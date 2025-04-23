import subprocess
import os

class NFIQ2:
    def __init__(self, nfiq2_path, model_path):
        """
        Initialize the NFIQ2 class with paths to the NFIQ2 executable and model file.
        
        :param nfiq2_path: Path to the NFIQ2 executable (e.g., './nfiq2').
        :param model_path: Path to the NFIQ2 model file (e.g., '/path/to/nist_plain_tir-ink.txt').
        """
        self.nfiq2_path = nfiq2_path
        self.model_path = model_path

    def get_quality_score(self, image_path):
        """
        Get the NFIQ2 quality score for a given fingerprint image.
        
        :param image_path: Path to the fingerprint image file (e.g., 'fp1.jpg').
        :return: NFIQ2 quality score as an integer.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"The image file {image_path} does not exist.")

        # Construct the command to run NFIQ2
        command = [self.nfiq2_path, "-m", self.model_path, image_path]

        try:
            # Debugging: Print paths
            print(f"NFIQ2 Path: {self.nfiq2_path}")
            print(f"Model Path: {self.model_path}")
            print(f"Image Path: {image_path}")

            # Run the command and capture the output
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)

            # Check if the command was successful
            if result.returncode != 0:
                print(f"NFIQ2 stderr: {result.stderr}")
                raise RuntimeError(f"NFIQ2 failed with error: {result.stderr}")

            # Extract the quality score from the output
            output = result.stdout.strip()
            print(f"NFIQ2 stdout: {output}")  # Debugging: Print NFIQ2 output
            quality_score = int(output.split()[-1])  # Assuming the score is the last part of the output
            return quality_score

        except subprocess.TimeoutExpired:
            raise RuntimeError("NFIQ2 execution timed out.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while running NFIQ2: {e}")

# Example usage
if __name__ == "__main__":
    # Paths to the NFIQ2 executable and model file
    nfiq2_path = "/home/bilal/Downloads/NFIQ2/build/install_staging/nfiq2/bin/nfiq2"
    model_path = "/home/bilal/Downloads/NFIQ2/build/install_staging/nfiq2/share/nist_plain_tir-ink.txt"
    image_path = "newfp1_output_1bit_.png"

    # Create an instance of the NFIQ2 class
    nfiq2 = NFIQ2(nfiq2_path, model_path)

    # Get the quality score
    try:
        score = nfiq2.get_quality_score(image_path)
        print(f"NFIQ2 Quality Score: {score}")
    except Exception as e:
        print(f"Error: {e}")
