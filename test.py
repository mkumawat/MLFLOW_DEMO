import mlflow
import warnings

# ignore all warning
warnings.filterwarnings("ignore")
def calculate(x,y):
    return (x*y)

if __name__ == "__main__":
    with mlflow.start_run():
        x,y=100,200
        result=calculate(x,y)
        print(f"here is my result {result}")
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_param("result",result)