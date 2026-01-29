class Node:
    def __init__(self, song_id):
        self.song_id = song_id
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_at_start(self, song_id):
        new_node = Node(song_id)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, song_id):
        new_node = Node(song_id)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_position(self, positions):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(postions - 1):
            if temp.next is None:
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def search_by_id(self, song_id):
        temp = self.head
        pos = 0
        while temp:
            if temp.song_id == song_id:
                return pos
            temp = temp.next
            pos += 1
        return -1

    def display(self):
        temp = self.head
        while temp:
            print(temp.song_id, end=" -> ")
            temp = temp.next
        print("None")


p = Playlist()
p.add_at_start(101)
p.add_at_end(102)
p.add_at_end(103)
p.add_at_start(100)
p.display()

print(p.search_by_id(102))

p.delete_by_position(2)
p.display()
problem title hospital taction cube arrangement system  A hospital emergency ward  the order arrived , the crtical patiant contaion indivusal persion can be forward in the patient impliment  tat support the following operation and end of new patieent in surch way thet come before order on same dischatde first patient distchrge patient id such patient display patient                        class Patient:
    def __init__(self, patient_id, severity):
        self.patient_id = patient_id
        self.severity = severity
        self.next = None

class EmergencyQueue:
    def __init__(self):
        self.head = None

    def insert_patient(self, patient_id, severity):
        new_node = Patient(patient_id, severity)
        if self.head is None or self.head.severity < severity:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next and temp.next.severity >= severity:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def discharge_first(self):
        if self.head:
            self.head = self.head.next

    def discharge_by_id(self, patient_id):
        if self.head is None:
            return
        if self.head.patient_id == patient_id:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.patient_id == patient_id:
                temp.next = temp.next.next
                return
            temp = temp.next

    def search_patient(self, patient_id):
        temp = self.head
        pos = 0
        while temp:
            if temp.patient_id == patient_id:
                return pos
            temp = temp.next
            pos += 1
        return -1

    def display_queue(self):
        temp = self.head
        while temp:
            print(f"[ID:{temp.patient_id}, Sev:{temp.severity}]", end=" -> ")
            temp = temp.next
        print("None")


q = EmergencyQueue()
q.insert_patient(101, 3)
q.insert_patient(102, 5)
q.insert_patient(103, 2)
q.insert_patient(104, 5)
q.insert_patient(105, 3)

q.display_queue()

q.discharge_first()
q.display_queue()

q.discharge_by_id(103)
q.display_queue()

print(q.search_patient(105))
