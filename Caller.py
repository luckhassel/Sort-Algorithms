from SortAlgorithmsCallers import SortAlgorithmsCallers

if __name__ == '__main__':
    sort_builder = SortAlgorithmsCallers()

    print("Ordering...")
    sort_builder.merge_sort()
    print("Merge Sort Done!")
    sort_builder.quick_sort()
    print("Quick Sort Done!")
    sort_builder.counting_sort()
    print("Counting Sort Done!")
    sort_builder.bubble_sort()
    print("Bubble Sort Done!")
    sort_builder.insertion_sort()
    print("Insertion Sort Done!")
    print("All Done!")





