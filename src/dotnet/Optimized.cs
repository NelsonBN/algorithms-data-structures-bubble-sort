namespace Demo;

public class Optimized
{
    public static void Run()
    {
        Console.WriteLine("Optimized:");
        var array = new int[] { 5, 3, 21, 13, 1, 7, 6, 15 };

        Console.WriteLine("Before: " + string.Join(", ", array));

        BubbleSort(array);

        Console.WriteLine("After: " + string.Join(", ", array));
    }

    public static void BubbleSort(int[] arr) // o(n^2)
    {
        for (int i = 0; i < arr.Length; i++) // n -> O(n)
        {
            var swapped = false;
            for (int j = 0; j < arr.Length - 1 - i; j++) // n * n -> O(n^2)
            {
                if (arr[j] > arr[j + 1]) // 1 * n * n -> O(n^2)
                {
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j]); // 1 * n * n -> O(n^2)
                    swapped = true;
                }
            }

            if (!swapped)
            {
                break;
            }
        }
    }
}
