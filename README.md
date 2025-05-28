## How to Use

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

2. **Add Dataset**

   * Place your dataset in YOLOv1 format inside the `./Dataset` directory.

3. **Update Model Name**

   * Open `trainer.py` and change the model name as needed.

4. **Run the Training Script**

   * Execute `trainer.py` to start training.
   * You can modify hyperparameters within the script as desired:

     ```bash
     python trainer.py
     ```


