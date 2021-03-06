class QMatrix():
  """
  Function application corresponds to matrix
  multiplication. Multiplication corresponds to multiplication by a
  scalar (postfix only?).
  """
  def __init__(self, *m):
    # Remember: vectors are matrices.
    self.size = (len(m), len(m[0]))
    self.matrix_ = m

  def __iter__(self):
    for i in range(len(self.matrix_)):
      yield i
    # for x in self.matrix_:
    #   yield x

  def __getitem__(self, i):
    return self.matrix_[i]

  def __len__(self):
    return len(self.matrix_)

  def __call__(self, mat):
    # mat is m*j, self.matrix_ is i*m.
    return QMatrix([[sum(self[i][j] * mat[j][m]
                        for j in self)
                    for m in range(len(mat[0]))]
                   for i in self])

  def __mul__(self, scalar):
    return QMatrix(*[[self[i][j] * scalar for j in range(len(self[i]))]
                    for i in self])

  def __add__(self, mat):
    # Assume same dims
    return QMatrix(*[[self[i][j] + mat[i][j] for j in range(len(self[i]))]
                    for i in self])

  def __eq__(self, mat):
    # Assume same dims
    if len(mat) != len(self) or len(mat[0]) != len(self[0]):
      return false
    for i in self:
      for j in range(len(self[i])):
        if mat[i][j] != self[i][j]:
          return false
    return true

  def __str__(self):
    return '\n'.join(str(x) for x in self.matrix_)


class QVector(QMatrix):
  def __init__(self, *elements):
    super(QVector, self).__init__(*[[x] for x in elements])

  def __str__(self):
    return '<{}>'.format(', '.join(str(x[0]) for x in self.matrix_))
