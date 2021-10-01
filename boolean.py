integer = int(input('Write a number: '))
def is_prime(integer):
    prime = False
    for getal in range(2, integer):
        if  integer % getal == 0:
            prime = False
            break
        else:
            prime = True
    return prime
def main():
    print(is_prime(integer))
main()
