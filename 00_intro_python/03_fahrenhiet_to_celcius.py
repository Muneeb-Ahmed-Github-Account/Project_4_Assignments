def main():

    fahrenhiet = float(input("\033[1;3m Enter tempreture in fahrenhiet \033[0m"))

    celsius = (fahrenhiet - 32 ) * 5.0/9.0

    print(f"Tempreture: {fahrenhiet}F = {celsius}C")

if __name__ == '__main__':
    main()