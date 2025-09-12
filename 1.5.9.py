"""CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)


Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory,
 максимум N - по числу слотов памяти на материнской плате (N = 4).

Объекты классов должны иметь следующие локальные свойства:

для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU;
 total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
 mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов
 на материнской плате в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).

P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям."""
class CPU:
    def __init__(self,name,fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self,name, volume):
        self.name = name
        self.volume = volume
class MotherBoard:
    def __init__(self,name,cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = args
    def get_config(self):
        #print(self.mem_slots)
        return ([f"Материнская плата: {self.name}",f"Центральный процессор: {self.cpu.name},{self.cpu.fr}",
              f"Слотов памяти: {self.total_mem_slots}", f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"])
        #print( [ f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"] )
cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, mem1, mem2)
#print(mb.__dict__)
#print(mem1)
#(mb.get_config())\


assert isinstance(mb, MotherBoard) and hasattr(MotherBoard, 'get_config')


def get_config():
    mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])

    return [f"Материнская плата: {mb.name}",
            f"Центральный процессор: {mb.cpu.name}, {mb.cpu.fr}",
            f"Слотов памяти: {mb.total_mem_slots}",
            f"Память: {mem_str}"]


res1 = ("".join(mb.get_config())).replace(" ", "")
res2 = ("".join(get_config())).replace(" ", "")
print( res1)
print(res2)
assert res1 == res2, "метод get_config возвратил неверные данные"
