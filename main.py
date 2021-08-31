from challenge import DataCapture

if __name__ == '__main__':
    capture = DataCapture()
    items = [3, 9, 3, 4, 6]
    for i in items:
        capture.add(i)

    stats = capture.build_stats()
    if stats:
        # Results
        print('Count of items less than 4: %s' % stats.less(4))
        print('Count of items between 3 and 6: %s' % stats.between(3, 6))
        print('Count of items greater than 4: %s' % stats.greater(4))
