import numpy as np 
import cv2


class Invertor:
    @staticmethod
    def _step(img:np.ndarray, **kwargs) -> np.ndarray:
        """
        This method for invert's the colors of an image.

        Parameters
        ----------
        img : np.ndarray
            default image which will be modified
            
        Returns
        -------
        modified_img : np.ndarray
            return modified image after operation
        """
        if kwargs:
            print(f"[invert] Unused arguments: {kwargs.keys()}!")

        return 255 - img