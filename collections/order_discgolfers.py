def order_discgolfers(scores):
    for key in sorted(scores.iterkeys()):

        print("%s: %s" % (key, scores[key]))

    return scores


scores = [{
    'bob': 3,
    'patric': 2,
    'squidward': 4,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 2,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}]
print(str(order_discgolfers(scores)))
