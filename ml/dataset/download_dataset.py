import kagglehub

path = kagglehub.dataset_download(
    "kushagrapandya/visdrone-dataset",
    output_dir="./dataset/visdrone"
)

print("Dataset downloaded to:", path)