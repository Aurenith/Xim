Xim/
│
├── api/                                  # FastAPI Backend
│   ├── app.py
│   ├── controllers/
│   ├── services/
│   ├── auth/
│   ├── lib/
│   └── requirements.txt
│
├── ml/                                   # Machine Learning
│   │
│   ├── environment.yml
│   │
│   ├── datasets/
│   │   │
│   │   ├── raw/                          # Downloaded datasets
│   │   │   ├── visdrone/
│   │   │   ├── bdd100k/
│   │   │   ├── exdark/
│   │   │   ├── iwildcam/
│   │   │   └── custom/
│   │   │
│   │   ├── intermediate/                 # Converted datasets
│   │   │   ├── visdrone_yolo/
│   │   │   ├── bdd100k_yolo/
│   │   │   ├── custom_yolo/
│   │   │   └── exdark_yolo/
│   │   │
│   │   └── final/                        # Final training dataset
│   │       ├── train/
│   │       │   ├── images/
│   │       │   └── labels/
│   │       │
│   │       ├── val/
│   │       │   ├── images/
│   │       │   └── labels/
│   │       │
│   │       └── test/
│   │           ├── images/
│   │           └── labels/
│   │
│   ├── configs/
│   │   └── dataset.yaml
│   │
│   ├── preprocessing/
│   │   ├── convert_annotations.py
│   │   ├── normalize_classes.py
│   │   ├── clean_dataset.py
│   │   ├── augment.py
│   │   ├── merge_datasets.py
│   │   └── split_dataset.py
│   │
│   ├── training/
│   │   ├── train.py
│   │   └── evaluate.py
│   │
│   ├── inference/
│   │   ├── detector.py
│   │   ├── predict.py
│   │   └── stream.py
│   │
│   ├── tracking/
│   │   └── tracker.py
│   │
│   ├── models/
│   │   ├── pretrained/
│   │   └── trained/
│   │       └── forest_surveillance/
│   │
│   ├── experiments/
│   └── README.md
│
├── shared/
├── assets/
├── compose.yaml
└── README.md