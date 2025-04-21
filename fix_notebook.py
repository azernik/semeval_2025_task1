import nbformat

path = "SemEval_Admire_UCSC.ipynb"

with open(path) as f:
    nb = nbformat.read(f, as_version=4)

if "widgets" in nb.metadata and "state" not in nb.metadata["widgets"]:
    del nb.metadata["widgets"]

with open(path, "w") as f:
    nbformat.write(nb, f)

print("Notebook fixed.")
