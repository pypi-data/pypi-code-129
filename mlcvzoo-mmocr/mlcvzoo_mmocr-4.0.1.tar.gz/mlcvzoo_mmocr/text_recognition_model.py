# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
Module for defining the model classes that are used to wrap the mmocr framework.
"""

import logging
from statistics import mean
from typing import Any, Dict, List, Optional, Tuple, Union

from mlcvzoo_base.api.data.ocr_perception import OCRPerception
from mlcvzoo_base.api.model import OCRModel
from nptyping import Int, NDArray, Shape

from mlcvzoo_mmocr.configuration import MMOCRConfig
from mlcvzoo_mmocr.model import MMOCRModel

logger = logging.getLogger(__name__)

ImageType = NDArray[Shape["Height, Width, Any"], Int]


class MMOCRTextRecognitionModel(
    MMOCRModel[OCRPerception],
    OCRModel[MMOCRConfig, Union[str, ImageType]],
):
    def __init__(
        self,
        from_yaml: str,
        configuration: Optional[MMOCRConfig] = None,
        string_replacement_map: Optional[Dict[str, str]] = None,
        init_for_inference: bool = False,
        is_multi_gpu_instance: bool = False,
    ) -> None:
        MMOCRModel.__init__(
            self,
            from_yaml=from_yaml,
            configuration=configuration,
            string_replacement_map=string_replacement_map,
            init_for_inference=init_for_inference,
            is_multi_gpu_instance=is_multi_gpu_instance,
        )
        OCRModel.__init__(
            self,
            unique_name=self.configuration.base_config.MODEL_SPECIFIER,
            configuration=self.configuration,
            init_for_inference=init_for_inference,
        )

    @staticmethod
    def __filter_result_score_by_mean(
        result: Dict[str, Any], score_threshold: float
    ) -> Optional[float]:
        """
        Take the result of the mmocr prediction and determine the
        score of the word

        Args:
            result: The result of the prediction
            score_threshold: The threshold for the score that has to be fulfilled

        Returns:
            The determined score
        """

        score: float = 0.0
        if isinstance(result["score"], list):
            # The list may be empty, therefore a dedicated check is needed
            if result["score"]:
                score = mean(result["score"])
        else:
            score = result["score"]

        return score if score >= score_threshold else None

    def predict(
        self, data_item: Union[str, ImageType]
    ) -> Tuple[Union[str, ImageType], List[OCRPerception]]:

        assert self.net is not None

        ocr_texts: List[OCRPerception] = []

        result = self._predict(data_item=data_item)

        score = self.__filter_result_score_by_mean(
            result=result,
            score_threshold=self.configuration.inference_config.score_threshold,
        )

        if score is not None:
            ocr_texts.append(OCRPerception(content=result["text"], score=score))

        return data_item, ocr_texts

    def predict_many(
        self, data_items: List[Union[str, ImageType]]
    ) -> List[Tuple[Union[str, ImageType], List[OCRPerception]]]:

        assert self.net is not None

        prediction_list: List[Tuple[Union[str, ImageType], List[OCRPerception]]] = []

        results = self._predict(data_item=data_items)

        for data_item, result in zip(data_items, results):

            score = self.__filter_result_score_by_mean(
                result=result,
                score_threshold=self.configuration.inference_config.score_threshold,
            )

            if score is not None:

                prediction_list.append(
                    (
                        data_item,
                        [OCRPerception(content=result["text"], score=score)],
                    )
                )
            else:
                prediction_list.append(
                    (
                        data_item,
                        [],
                    )
                )

        return prediction_list
