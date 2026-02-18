import argparse
import sys
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to extract dominant color(s) from images via KMeans clustering on RGB pixels."
    )
    parser.add_argument("image", help="Path to the input image file")
    parser.add_argument(
        "--num-colors",
        "-n",
        type=int,
        default=1,
        help="Number of dominant colors to extract (default: 1)"
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["rgb", "hex"],
        default="rgb",
        help="Output format: 'rgb' or 'hex' (default: rgb)"
    )
    args = parser.parse_args()

    if args.num_colors < 1:
        parser.error("--num-colors must be a positive integer.")

    try:
        img = Image.open(args.image).convert("RGB")
    except FileNotFoundError:
        print(f"Error: No such file: {args.image}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading image '{args.image}': {e}", file=sys.stderr)
        sys.exit(1)

    data = np.array(img).reshape((-1, 3))
    total_pixels = data.shape[0]
    if total_pixels == 0:
        print("Error: Image contains no pixels.", file=sys.stderr)
        sys.exit(1)

    n_clusters = min(args.num_colors, total_pixels)
    if n_clusters < args.num_colors:
        print(
            f"Warning: Capping to {n_clusters} clusters "
            f"(image has only {total_pixels:,} pixels).",
            file=sys.stderr
        )

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )
    kmeans.fit(data)

    centers = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    unique, counts = np.unique(labels, return_counts=True)
    sort_idx = np.argsort(counts)[::-1]

    for idx in sort_idx:
        color = tuple(centers[idx])
        count = counts[idx]
        percentage = (count / total_pixels) * 100

        if args.format == "rgb":
            color_str = f"({color[0]}, {color[1]}, {color[2]})"
        else:  # hex
            color_str = f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}"

        print(f"{color_str} ({percentage:.1f}%)")

if __name__ == "__main__":
    main()
