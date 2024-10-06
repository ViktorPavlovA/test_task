import numpy as np
import cv2

class Light_Leveling:
    @staticmethod
    def _step(img:np.ndarray, clip_limit:int = 2, tile_grid_size:tuple = (8,8), **kwargs) -> np.ndarray:
        """
        This Method for adjusts the light level of an image.

        Parameters
        ----------
        img : np.ndarray
            default image which will be modified
        clip_limit : int, optional
            contrast parameter, by default 2
        tile_grid_size : tuple, optional
            tile size for clahe function, by default (8,8) kernel size 

        Returns
        -------
        modified_img : np.ndarray
            return modified image after operation
        
        """
        if len(kwargs) > 0:
            print(f"[light_leveling] Unused arguments: {kwargs.keys()}!")

        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        c_l, c_a, c_b = cv2.split(img)
        c_l = clahe.apply(c_l)
        img = cv2.merge((c_l, c_a,c_b))

        return cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
