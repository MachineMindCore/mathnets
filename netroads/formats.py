from typing import List

NATURALPROOFS = {
    "dataset": {
        
        "theorems": {
            "id": int, 
            "type": str, 
            "label": str, 
            "title": str, 
            "categories": List[str], 
            "contents": List[str], 
            "refs": List[str], 
            "ref_ids": List[int], 
            "proofs": {
                "contents": List[str],
                "refs": List[str],
                "ref_ids": List[int]
            }
        },
        
        "definitions": {
            "id": int, 
            "type": str, 
            "label": str, 
            "title": str, 
            "categories": List[str], 
            "contents": List[str], 
            "refs": List[str], 
            "ref_ids": List[int]
        },

        "others": {
            "id": int, 
            "type": str, 
            "label": str, 
            "title": str, 
            "categories": List[str], 
            "contents": List[str], 
            "refs": List[str], 
            "ref_ids": List[int]
        },

        "retrieval_examples": List[int],
    
    },

    "splits": {
        
        "train": {
            "ref_ids": List[int],
            "examples": List[List[int]]
        },

        "valid": {
            "ref_ids": List[int],
            "examples": List[List[int]]
        },

        "test": {
            "ref_ids": List[int],
            "examples": List[List[int]]
        },
    }
}
