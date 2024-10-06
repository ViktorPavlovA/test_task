"""
Example of using the pipeline module
"""

import numpy 
import cv2

from modules.pipeline_module import PipelineModule

if __name__ == "__main__":

    image = cv2.imread("./photo/test.png")

    pipeline = [{"name": "resize", "args": {"scale_percent": 50,"interpolation": cv2.INTER_CUBIC}},
                {"name": "light_leveling", "args": {"clip_limit": 2, "tile_grid_size": (8, 8)}},
                {"name": "binarization", "args": {"threshold": 80}},
                {"name": "invert", "args": {}}]
    
    processed_image = PipelineModule.start_pipeline(image.copy(), pipeline)

    cv2.imshow("Original Image", image)
    cv2.imshow("Processed Image", processed_image)
    cv2.waitKey(0)