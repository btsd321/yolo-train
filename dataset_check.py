from ultralytics.data.utils import visualize_image_annotations


label_map = {  # Define the label map with all annotated class labels.
    0: "target",
}

# Visualize
visualize_image_annotations(
    "dataset/images/train/20250326_215453_0dXxQ6Vp.jpg",  # Input image path.
    "20250326_215453_0dXxQ6Vp.txt",  # Annotation file path for the image.
    label_map,
)