import numpy as np
import cv2

class Resizer:
    @staticmethod
    def _step(img:np.ndarray, scale_percent:int = 50, interpolation=cv2.INTER_CUBIC, **kwargs) -> np.ndarray:
        """
        This method will apply binarization to the image

        Parameters
        ----------
        img : np.ndarray
            default image which will be modified
        scale_percent:int, : int,
            scale percent to resize image 
        interpolation : optional
            interpolation method, by default cv2.INTER_CUBIC

        Returns
        -------
        modified_img : np.ndarray
            return modified image after operation
        """
        if len(kwargs) > 0:
            print(f"[resize] Unused arguments: {kwargs.keys()}!")

        w = int(img.shape[1] * scale_percent / 100)
        h = int(img.shape[0] * scale_percent / 100)
        dim = (w, h)

        return cv2.resize(img, dim, interpolation = interpolation)