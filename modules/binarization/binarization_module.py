import numpy as np
import cv2


class Binarizator:
    @staticmethod
    def _step(img:np.ndarray, threshold:int=80, **kwargs) -> np.ndarray:
        """
        This method will apply binarization to the image

        Parameters
        ----------
        img : np.ndarray
            default image which will be modified
        threshold : int, optional
            threshold value for binarization, by default 50

        Returns
        -------
        modified_img : np.ndarray
            return modified image after operation
        """
        if kwargs:
            print(f"[binarization] Unused arguments: {kwargs.keys()}!")

        if threshold >= 0 and threshold <= 255:
            modified_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, modified_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
            if ret: 
                return modified_img 
        else:
            print("Threshold value must be between 0 and 255. Return input frame!")
        return img