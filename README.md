# Recommendation Model for Educational Courses

## Overview
This repository contains the implementation of a recommendation model for educational courses, based on the Llama 3 model. The goal of the project is to suggest courses to users by analyzing the data stored in a JSON file containing course information and metadata. The recommendations will be displayed in a format similar to the example provided in the attached project plan.

## Key Features
- **Course Recommendation**: The model suggests courses tailored to user preferences and needs.
- **Integration with Llama 3**: Utilizes the power of Llama 3 for natural language understanding and enhanced recommendation logic.
- **JSON Data Handling**: Reads and processes course data stored in a JSON file.
- **User-Friendly Interface**: Recommendations are displayed in a structured and visually appealing format.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/recommendation-model.git
   cd recommendation-model
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your course JSON file to the `data/` directory.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- [Llama 3](https://ai.meta.com/llama/) for providing the base model.
- Members of our academic research group for their valuable feedback and support.

# How to run the file

The `Training_LLAMA.ipynb` file was created to train the model on the basis of the LLAMA model.

The `Run_model.ipynb` file was created to use model. We need to complete the last cell by specifying which course topics we are interested in.

In both cases, we just need to add the google colab defined key with hugging_face.