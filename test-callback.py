def callback(sum):
    print("Sum = {}".format(sum))

def main(a, b, callback = None):
    print("adding {} + {}".format(a, b))
    if callback:
        callback(a+b)

main(7, 2, callback)
