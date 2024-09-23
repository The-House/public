import os
from rasa.__main__ import main

if __name__ == '__main__':
    # You can set any environment variables here
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Example for GPU handling (if applicable)

    # Run Rasa server
    main(["run", "--enable-api", "--cors", "*", "--debug"])
