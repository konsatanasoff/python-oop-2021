class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)

    @staticmethod
    def find_element(category_id, search_from):
        return [el for el in search_from if el.id == category_id][0]

    @staticmethod
    def check_and_remove(item, location_list):
        if item in location_list:
            location_list.remove(item)
        return location_list

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.find_element(category_id, self.categories)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.find_element(topic_id, self.topics)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, doc_id, new_file_name):
        document = self.find_element(doc_id, self.documents)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.find_element(category_id, self.categories)
        self.categories = self.check_and_remove(category, self.categories)

    def delete_topic(self, topic_id):
        topic = self.find_element(topic_id, self.topics)
        self.topics = self.check_and_remove(topic, self.topics)

    def delete_document(self, doc_id):
        document = self.find_element(doc_id, self.documents)
        self.documents = self.check_and_remove(document, self.documents)

    def get_document(self, doc_id):
        return self.find_element(doc_id, self.documents)


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
