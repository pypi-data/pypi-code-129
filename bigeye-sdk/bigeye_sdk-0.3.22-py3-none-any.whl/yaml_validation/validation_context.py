from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Union

from bigeye_sdk.exceptions.exceptions import FileLoadException
from bigeye_sdk.log import get_logger
from bigeye_sdk.yaml_validation.validation_models import FileMatchResult, ValidationError

log = get_logger(__file__)


@dataclass
class ValidationContext:
    _BIGEYE_YAML_FILE_IX: Dict[str, Dict[int, str]] = field(default_factory=dict)  # { file_name: { line_number: line }}
    _VALIDATION_ERROR_IX: Dict[
        str, List[ValidationError]] = field(default_factory=dict)  # {erroneous_configuration_cls_name: ValidationError}
    _FILE_ERROR_MATCH_RESULT_IX: Dict[
        str, Dict[int, List[FileMatchResult]]] = field(
        default_factory=dict)  # {file_name: {file_start_loc: file_match_results}}

    def _testcase_support_clear_validation_context(self):
        self._VALIDATION_ERROR_IX: Dict[str, List[ValidationError]] = {}
        self._BIGEYE_YAML_FILE_IX: Dict[str, Dict[int, str]] = {}
        self._FILE_ERROR_MATCH_RESULT_IX: Dict[str, Dict[int, List[FileMatchResult]]] = {}

    def put_bigeye_yaml_file_to_ix(self, file_name: str) -> Dict[str, Dict[int, str]]:
        current_line_number = 0

        file_contents: Dict[int, str] = {}

        with open(file_name, 'r') as fin:
            for line in fin:
                current_line_number = current_line_number + 1
                file_contents[current_line_number] = line

        if file_name in self._BIGEYE_YAML_FILE_IX.keys():
            raise FileLoadException(f"Duplicate file found: {file_name}")

        self._BIGEYE_YAML_FILE_IX[file_name] = file_contents

        return self._BIGEYE_YAML_FILE_IX

    def put_validation_error_to_ix(self, ve: ValidationError):
        if ve.erroneous_configuration_cls_name in self._VALIDATION_ERROR_IX.keys():
            self._VALIDATION_ERROR_IX[ve.erroneous_configuration_cls_name].append(ve)
        else:
            self._VALIDATION_ERROR_IX[ve.erroneous_configuration_cls_name] = [ve]

    def put_file_error_match_result_to_ix(self, fmr: FileMatchResult):
        line_number = min(fmr.lines)
        if fmr.file_name in self._FILE_ERROR_MATCH_RESULT_IX.keys():
            """if file name key exists?"""
            if min(fmr.lines) in self._FILE_ERROR_MATCH_RESULT_IX[fmr.file_name]:
                self._FILE_ERROR_MATCH_RESULT_IX[fmr.file_name][line_number].append(fmr)
            else:
                self._FILE_ERROR_MATCH_RESULT_IX[fmr.file_name][min(fmr.lines)] = [fmr]
        else:
            """if file name key does not exist"""
            self._FILE_ERROR_MATCH_RESULT_IX[fmr.file_name] = {}
            self._FILE_ERROR_MATCH_RESULT_IX[fmr.file_name][line_number] = [fmr]

    def get_validation_errors(self,
                              configuration_cls_name: str = None
                              ) -> Union[Dict[str, List[ValidationError]], List[ValidationError]]:
        if not configuration_cls_name:
            return self._VALIDATION_ERROR_IX
        else:
            return self._VALIDATION_ERROR_IX.get(configuration_cls_name, [])

    def get_file_error_match_results(self,
                                     file_name: str = None
                                     ) -> Union[
        Dict[str, Dict[int, List[FileMatchResult]]],
        Dict[int, List[FileMatchResult]]
    ]:
        if not file_name:
            return self._FILE_ERROR_MATCH_RESULT_IX
        else:
            return self._FILE_ERROR_MATCH_RESULT_IX[file_name]

    def generate_fixmes(self, output_path: str):
        log.info('Generating FixMe files.')
        for file_name, file_match_result_ix in self._FILE_ERROR_MATCH_RESULT_IX.items():
            with open(f'{output_path}/FIXME_{Path(file_name).name}', 'w') as fout:
                for line_number, line in self._BIGEYE_YAML_FILE_IX[file_name].items():
                    if line_number in file_match_result_ix.keys():
                        """If error exists for line then print report inline."""
                        fout.write('>>>>')

                        fmr: FileMatchResult
                        for fmr in file_match_result_ix[line_number]:
                            fout.write('\n')
                            fout.write(fmr.error_message)
                            fout.write('\n')

                        fout.write('<<<<')
                        fout.write('\n')

                    fout.write(line)


    @classmethod
    def lines_match(cls, search: str, content: str) -> bool:
        c = content
        if len(content) > 1 and len(search) > 1 and content.strip()[0] == '-' and search.strip()[0] != '-':
            "matching object without list indicator"
            c = content.strip()[1:]
        if ':' in content and ':' not in search:
            "matching value against dictionary"
            c = c.split(':')[-1] # split on : to take value of yaml k/v pair.
        is_match = cls.cleanse_line(search) == cls.cleanse_line(c)
        return is_match

    @classmethod
    def cleanse_line(cls, l: str) -> str:
        r = l
        r = re.sub(r'\s*#(.*)\s*#(.*)|#(.*)[^#]*', '', r)  # remove comments
        r = r.strip()  # strip all leading and trailing spaces.emoves comments and strips spcaces.
        return r

    @classmethod
    def is_only_comment(cls, l: str) -> bool:
        p = re.compile(r'\s*#(.*)\s*#(.*)|#(.*)[^#]*')
        return re.fullmatch(p, l.strip()) is not None and not cls.cleanse_line(l)

    @classmethod
    def search_lines_in_source_lines(cls,
                                     search_lines: List[str],
                                     source_lines: Dict[int, str]) -> List[Dict[int, str]]:
        """
        Search for lines (full block) within another set of lines.  Accommodates new lines in the source if not within
        the search block of lines -- capture yaml serialization differences.
        Args:
            search_lines: Block of lines to search for.
            source_lines: Block of lines to search within.

        Returns: A list of line blocks that match the search criteria.

        """

        matching_lines_sets: List[Dict[int, str]] = []
        matching_lines: Dict[int, str] = {}

        search_line_matched_ix = 0

        def get_current_search_string():
            return search_lines[search_line_matched_ix]

        for line_number, line in source_lines.items():

            if search_line_matched_ix < len(search_lines):
                """for testing"""
                css = get_current_search_string()

            if len(matching_lines.keys()) == len(search_lines):
                "when the match line count is equal to search line count"
                # if include_contains_search and any(a in b for a, b in zip(search_lines, matching_lines.values())):
                #     matching_lines_sets.append(matching_lines)
                if any(cls.lines_match(search=a, content=b)
                       for a, b in zip(search_lines, matching_lines.values())):
                    matching_lines_sets.append(matching_lines)

                search_line_matched_ix = 0
                matching_lines = {}
            elif cls.lines_match(search=search_lines[0], content=line):
                "restarting when we find a line matching the first."
                matching_lines = {line_number: line}
                search_line_matched_ix = 1
            elif cls.lines_match(search=get_current_search_string(), content=line):
                "appending lines that match."
                search_line_matched_ix = search_line_matched_ix + 1
                matching_lines[line_number] = line
            elif (line.isspace() or cls.is_only_comment(line)) and not get_current_search_string().isspace() \
                    and matching_lines:
                "skipping unexpected newlines in match"
                pass
            elif not cls.lines_match(search=get_current_search_string(), content=line):
                "resetting if we find a line that doesnt match."
                search_line_matched_ix = 0
                matching_lines = {}

        return matching_lines_sets

    def search_validation_errors_in_files(self):
        for ves in self._VALIDATION_ERROR_IX.values():
            for ve in ves:
                self.search_validation_error_in_files(ve)

    def search_validation_error_in_files(self, ve: ValidationError) -> ValidationError:

        file_match_results: List[FileMatchResult] = []

        if ve.error_context_lines:
            search_lines = ve.error_context_lines
            is_error_context_search = True
        else:
            search_lines = ve.error_lines
            is_error_context_search = False

        for file_name, file_content in self._BIGEYE_YAML_FILE_IX.items():
            matching_lines_sets = self.search_lines_in_source_lines(search_lines=search_lines,
                                                                    source_lines=file_content)

            if is_error_context_search:
                """Match all error_lines to each matched error_content_lines."""
                context_sets = matching_lines_sets
                matching_lines_sets: List[Dict[int, str]] = []

                for mls in context_sets:
                    found_sub_matches = self.search_lines_in_source_lines(
                        search_lines=ve.error_lines,
                        source_lines=mls
                    )
                    matching_lines_sets.extend(found_sub_matches)

            fmrs: List[FileMatchResult] = []

            for m in matching_lines_sets:
                fmr = FileMatchResult(file_name=file_name, lines=m, error_message=ve.error_message)
                fmrs.append(fmr)
                self.put_file_error_match_result_to_ix(fmr)

            file_match_results.extend(fmrs)

        return ve
