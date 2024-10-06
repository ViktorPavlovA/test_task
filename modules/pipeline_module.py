import numpy as np

from modules import Binarizator, Invertor, Resizer, Light_Leveling


class PipelineModule:
    @staticmethod
    def start_pipeline(img:np.ndarray,pipeline_list:list[str]) -> np.ndarray:
        """
        This method will apply all the operations in setup_list to img

        Parameters
        ----------
        img : np.ndarray
            default image which will be modified
        setup_list : list[str]
            list of base operation which will be applied to img

        Returns
        -------
        modified_img : np.ndarray
            return modified image which depends on setup_list

        See Also
        --------
        Available operations are: 
        
        * resize
        * light_leveling
        * binarization
        * invert

        """

        if img is None:
            print("Image is None!")
            return None

        operations = {
        "resize": Resizer._step,
        "light_leveling": Light_Leveling._step,
        "binarization": Binarizator._step,
        "invert": Invertor._step
        }
        
        for operation in pipeline_list:
            op_name = operation.get("name")
            op_args = operation.get("args")
            if op_name in operations:
                img = operations[op_name](img, **op_args)
            else:
                print(f"Unknown operation type: {operation}!")
                print(f"Available operations are: {list(operations.keys())}")

        return img
    


    
