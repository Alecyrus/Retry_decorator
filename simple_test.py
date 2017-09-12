from retry_decorator import retry


@retry([ZeroDivisionError], verbose=True)
def div(a,b):
    return a/b



if __name__ == "__main__":
    print("The simple test for the Retry Decorator.")

    print("The Function for testing:\n")
    print("""
    @retry([ZeroDivisionError], verbose=True)
    def div(a,b):
        return a/b

    """)
    try:
        print("Output:\n")
        print(div(1, 0))

    except Exception as e:
        print("The exception is catched.", e)
