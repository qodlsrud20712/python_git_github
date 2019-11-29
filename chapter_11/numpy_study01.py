import numpy

def seq_array():
    data1 = list(range(0, 10))
    print(type(data1), data1)
    a1 = numpy.array(data1)
    print(type(a1), a1.dtype, a1)
    print(a1[1])

    data2 = [0.1, 5, 4, 12, 0.5]
    a2 = numpy.array(data2)
    print(a2.dtype, a2)


def arange_array():
    print(numpy.arange(0, 10, 2))
    print(numpy.arange(1, 10))
    print(numpy.arange(5))

    a = numpy.arange(12).reshape(4, 3)
    print('2차원배열', a)
    print('2차원 행열갯수', a.shape)
    a2 = numpy.arange(5)
    print('1차원배열', a2.shape)


def two_dimension_array():
    a3 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a3.dtype, a3)


def num_array():
    print(numpy.linspace(1, 10, 10))
    print(0, numpy.pi, 20)
    print(numpy.zeros(10))
    print(numpy.zeros((3, 4)))
    print(numpy.ones(5))
    print(numpy.ones((3, 5)))
    print(numpy.eye(3))


def type_conversion():
    str_array = numpy.array(['1.5', '0.62', '2', '3.14', '3.141592'])
    print(str_array, str_array.dtype)
    float_array = str_array.astype(float)
    print(float_array, float_array.dtype)


def random_array():
    print(numpy.random.rand(2, 3))
    print(numpy.random.rand(2, 3, 4))
    print(numpy.random.randint(10, size=(3, 4)))
    print()
    print(numpy.random.randint(1, 30))


def array_operation():
    arr1 = numpy.array([10, 20, 30, 40])
    arr2 = numpy.array([1, 2, 3, 4])
    print('더하기:{}, 뺴기:{}, 배열 값 각각 곱하기:{}, 거듭제곱:{}, '
          '배열전체 곱하기:{}, 나누기:{}'.format(arr1 + arr2, arr1 - arr2, arr2 * 2, arr2 ** 2, arr1 * arr2, arr1 / arr2))
    print()
    print('복합연산:{}, 비교연산:{}'.format(arr1 / (arr2 ** 2), arr1 > 20))
    print()


def statistics_array():
    arr3 = numpy.arange(5)
    print('{} 더하기:{} 평균:{}'.format(arr3, arr3.sum(), arr3.mean()))
    print()
    print('표준편차:{} 분산:{}'.format(arr3.std(), arr3.var()))
    print()
    print('최솟값:{} 최댓값:{}'.format(arr3.min(), arr3.max()))
    print()

    arr4 = numpy.arange(1, 5)
    print('{} 누적합:{}\n 누적곱:{}\n'.format(arr4, arr4.cumsum(), arr4.cumprod()))


def matrix_operation():
    A = numpy.array([0, 1, 2, 3]).reshape(2, 2)
    B = numpy.array([3, 2, 0, 1]).reshape(2, 2)
    print('A:{}\n B:{} '.format(A, B))
    print('행렬곱:{}\n 전치행렬:{}\n 역행렬:{}\n 행렬식:{}'.format(numpy.dot(A, B), numpy.transpose(A), numpy.linalg.inv(A),
                                                   numpy.linalg.det(A)), end='\n')


def array_indexing():
    a1 = numpy.array([0,10,20,30,40,50])
    a2 =numpy.arange(10,100,10).reshape(3,3)
    a = numpy.array([1,2,3,4,5,6])
    print('{}, {}, {}'.format(a1, a1[0], a1[[1,3,4]]))
    print('{},{},{}'.format(a2, a2[0,2], a2[1]))
    print(a2[[0,2], [0,1]])
    print('{} {}'.format(a[a>3], a[(a%2)==0]))


def array_slicing():
    b1 = numpy.array([0,10,20,30,40,50])
    print('{}'.format(b1[1:4]))
    b1[3:6] = 60
    print(b1)
    b2 = numpy.arange(10,100,10).reshape(3,3)
    print('{},{},{}'.format(b2, b2[:3,1:], b2[1][0:2]))
    b2[0:2, 1:3] = numpy.array([[25,35], [55,65]])
    print(b2)

if __name__ == '__main__':
    seq_array()
    two_dimension_array()
    arange_array()
    num_array()
    type_conversion()
    random_array()
    array_operation()
    statistics_array()
    matrix_operation()
    array_indexing()
    array_slicing()
