import matplotlib.pyplot as plt

def plot_examples(images, figsize=(12, 6)):
    plt.figure(figsize=figsize)
    
    for i, img in enumerate(images):
        plt.subplot(1, len(images), i + 1)
        if hasattr(img, "permute"):   # tensor
            img = img.permute(1, 2, 0).cpu().numpy()
        plt.imshow(img)
        plt.axis("off")

    plt.tight_layout()
    plt.show()
