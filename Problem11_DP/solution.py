class ColorMatrix (object):

    def __init__(self, order_):
        self.MAX_T = 100
        self.COLORS = {"R":0,"G":1,"B":2}
        self.order = order_
        self.matrix = []
        self.dp_mem = {}
        self.tmp_snapshot = []
        self._read_matrix()
        self._initialise_dp_matrix()

    def _read_matrix(self):
        for _ in range(self.order):
            self.matrix.append(map(int,raw_input().split()))

    def _initialise_snapshot_at_t(self, t):
        self.tmp_snapshot = []
        for row_ in self.matrix:
            self.tmp_snapshot.append([(t/ele_%3) for ele_ in row_])

    def _initialise_dp_matrix_at_t_n_c(self, time_, color_):
        to_return = [[0 for _ in range((self.order+1))] for _ in range((self.order+1))]
        for val_row in range(1,self.order+1):
            for val_col in range(1,self.order+1):
                to_return[val_row][val_col] = (to_return[val_row-1][val_col]+
                to_return[val_row][val_col-1]-to_return[val_row-1][val_col-1])
                if self.tmp_snapshot[val_row-1][val_col-1]==color_:
                    to_return[val_row][val_col]+=1
        self.dp_mem["{}_{}".format(time_,color_)] = to_return

    def _initialise_dp_matrix(self):
        for time_ in range(1,self.MAX_T):
            # Create snapshot of matrix at time_
            self._initialise_snapshot_at_t(time_)
            for color_ in range(3):
                self._initialise_dp_matrix_at_t_n_c(time_, color_)

    def get_color_count(self, query_ele_):
        req_dp_matrix =  self.dp_mem["{}_{}".format(query_ele_[0],self.COLORS[query_ele_[5]])]
        x1,y1,x2,y2 = map(int,query_ele_[1:5])
        return (req_dp_matrix[x2][y2]-
        req_dp_matrix[x1-1][y2]-
        req_dp_matrix[x2][y1-1]+
        req_dp_matrix[x1-1][y1-1])

if __name__ == "__main__":
    meta = map(int,raw_input().split())
    color_matrix = ColorMatrix(meta[0])
    for _ in range(meta[1]):
        in_ = raw_input().split()
        print color_matrix.get_color_count(in_)
