from clang.cindex import Index, CursorKind, StorageClass

from optparse import OptionParser, OptionGroup
import json


def dump_global_var_decls(args):
    index = Index.create()
    tu = index.parse(None, args)
    if not tu:
        raise RuntimeError("unable to load input")

    def find_var_decls(node):
        if node.kind == CursorKind.VAR_DECL:
            info = {
                'location': f'{node.location.file}:{node.location.line}:{node.location.column}',
                'spelling': node.spelling,
                # 'type': node.type,
                # 'const': node.type.is_const_qualified(),
                # 'storage_class': str(node.storage_class),
                # 'semantic_parent': str(node.semantic_parent.kind),
            }

            is_const = node.type.is_const_qualified()
            is_static = node.storage_class == StorageClass.STATIC
            is_file_scope = node.semantic_parent.kind == CursorKind.TRANSLATION_UNIT

            is_bad = not is_const and (is_static or is_file_scope)

            info['is_bad'] = is_bad
            # print(info)
            print(json.dumps(info, indent=4))

        for c in node.get_children():
            find_var_decls(c)

    find_var_decls(tu.cursor)


def main():
    parser = OptionParser("usage: %prog [options] {filename} [clang-args*]")
    parser.disable_interspersed_args()
    (opts, args) = parser.parse_args()
    if len(args) == 0:
        parser.error('invalid number of arguments')

    dump_global_var_decls(args)


if __name__ == "__main__":
    main()
