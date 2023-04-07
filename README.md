# Dataset Visualizer

This is a simple tool to visualize the dataset. It can be used to visualize any dataset and can be proved beneficial for expolaratory data analysis.

## Usage

Streamlit is used to create the web app. To run the app, run the following command:

```bash
streamlit run app.py
```

## Dataset

The dataset used in this project is the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris). It is a multivariate dataset with 150 instances and 4 features. The dataset is available at the `root` directory.

You can, however, use any dataset of your choice. To do so, simply upload any dataset into the application and it will be used to visualize the dataset. The dataset should be in the `.csv` or `.txt` format.

## Features

The following features are available in the application:

-   **Dataset**: The dataset can be uploaded into the application. The dataset should be in the `.csv` or `.txt` format.
-   **Dataset Preview**: The dataset can be previewed in the application. The number of rows to be previewed can be specified.
-   **Dataset Statistics**: The dataset statistics can be viewed in the application. The statistics include the mean, median, mode, standard deviation, variance, minimum, maximum, and the number of missing values.
-   **Dataset Visualization**: The dataset can be visualized in the application. The following visualizations are available:
    -   **Histogram**: The histogram of the dataset can be viewed.
    -   **Bar Plots**: The box plot of the dataset can be viewed.
    -   **Count Plot**: The count plot of the dataset can be viewed.
    -   **Correlation Plot**: The correlation plot of the dataset can be viewed.
    -   **Heatmap**: The heatmap of the dataset can be viewed.

## Requirements

The following libraries are required to run the application:

-   [streamlit](https://streamlit.io/)
-   [pandas](https://pandas.pydata.org/)
-   [numpy](https://numpy.org/)
-   [matplotlib](https://matplotlib.org/)
-   [seaborn](https://seaborn.pydata.org/)
-   [plotly](https://plotly.com/python/)

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE)

## Author

[Abhisek Ganguly](https://github.com/abhisekganguly)

## Contribution

This project is open for contribution. Make a fork of the project and create a pull request to contribute to the project.