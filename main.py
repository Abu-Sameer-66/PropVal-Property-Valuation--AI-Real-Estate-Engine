from src.processor import RealEstateValuator
import sys

def main():
    print("Initializing Valuation Engine...")
    
    # robust path handling could be added here, assuming relative paths for now
    valuator = RealEstateValuator(
        train_path='data/train.csv', 
        test_path='data/test.csv'
    )

    try:
        print("Preprocessing data...")
        valuator.preprocess()
        
        print("Training model...")
        metrics = valuator.train()
        
        print("-" * 30)
        print(f"Model Results:")
        print(f"RMSE: {metrics['rmse']:.4f}")
        print(f"R2 Score: {metrics['r2']:.4f}")
        print("-" * 30)
        
        valuator.predict_submission('housing_submission.csv')
        
    except FileNotFoundError:
        print("Error: train.csv or test.csv not found in 'data/' directory.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()