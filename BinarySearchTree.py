class BST:

    def __init__(self, root):
        self.root = root        # 一開始設的值當為主鍵, root
        self.leftchild = None   # 左節點為空
        self.rightchild = None  # 右節點為空

    def insert(self, data):
        if self.root:                              # 如果root有值
            if data > self.root:                   # 輸入的數值大於root
                if self.rightchild is None:        # 先檢查右節點是否為空
                    self.rightchild = BST(data)    # 空的話, 創一個節點給右邊節點
                else:
                    self.rightchild.insert(data)   # 不為空的話, 直接insert進去
            elif data < self.root:                 # 輸入的數值小於root
                if self.leftchild is None:         # 先檢查左節點是否為空
                    self.leftchild = BST(data)     # 空的話, 創一個節點給左邊節點
                else:
                    self.leftchild.insert(data)    # 不為空的話, 直接insert進去

    def find(self, data):
        if data < self.root:                       # data小於主鍵的話
            if self.leftchild is None:             # 如果左節點沒東西, 直接return
                return print(data, "not found.")
            return self.leftchild.find(data)       # 繼續尋找左節點的方向
        elif data > self.root:                     # data大於主鍵的話
            if self.rightchild is None:            # 如果右節點沒東西, 直接return
                return print(data, "not found.")
            return self.rightchild.find(data)       # 繼續尋找右節點的方向
        else:
            print(data, "is found.")                # data == root 的時候就找到了

