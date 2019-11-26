class Car():
    instance_count = 0 #class 변수

    def __init__(self, size=10, color='black'):
        self.size = size        #slef써주면 인스턴수 변수
        self.color = color      #인스턴수 변수
        Car.instance_count = Car.instance_count+1
        print('자동차 생산대수:{}'.format(Car.instance_count))

    def __str__(self) -> str:
        return 'color {} size {}'.format(self.color, self.size)


    def set_speed(self, speed):
        self.speed = speed


    @staticmethod
    def check_type(model_code):
        if model_code >= 20:
            print('이 자동차는전기차.')
        elif 10<= model_code <20:
            print('이 자동차는 가솔린')
        else:
            print('이 자동차는 디젤차')


    @classmethod
    def count_instance(cls):
        print('자동차 생산대수:{}'.format(cls.instance_count))

    def auto_cruse(self):
        print('자율주행모드')
        print('{} 속도로 자율주행'.format(self.speed))

