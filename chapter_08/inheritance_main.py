from chapter_08.inheritance_study import Bicycle, FoldingBicycle

if __name__ == '__main__':
    myBicycle = Bicycle(wheel_size=26, color= 'red')
    myFoldBicycle = FoldingBicycle(wheel_size=30, color='blue')

    cycle_list = [myBicycle, myFoldBicycle]

    #[cycle.move(30) for cycle in cycle_list]
    [cycle.stop() for cycle in cycle_list]

    # myFoldBicycle.move(20)
    # myFoldBicycle.fold()
    # myFoldBicycle.unfold()
