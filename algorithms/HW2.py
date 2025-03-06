"""Пример создания стека через ООП"""


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def stack_del_duplicates(self):
        return list(set(self.elems))

    def find_middle(self):
        return self.elems[(len(self.elems) // 2)]

    def concat_stack(self, other):
        new_stack = self.elems + other.elems
        return new_stack

if __name__ == '__main__':

    SC_OBJ = StackClass()
    SC_OBJ_2 = StackClass()
    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)

    SC_OBJ_2.push_in(10)
    SC_OBJ_2.push_in('code')
    SC_OBJ_2.push_in(False)
    SC_OBJ_2.push_in(5.5)

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 5.5

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 4

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3

    # удаляем дубли
    # print(SC_OBJ.stack_del_duplicates()) # -> {'code', False, 10, 5.5}

    print(SC_OBJ.find_middle())

    new_sc = SC_OBJ.concat_stack(SC_OBJ_2)
    print(new_sc)