class tsSimClass:
    '''
    Class definition for time series simulator
    '''
    ## dunder methods (more later)
    def __init__(self, times, mean = 0, cor_param = 1, seed = 1):
        ## This is the constructor, called when `tsSimClass(...)` is invoked
        ## to create an instance of the class.

        ## For robustness, need checks that `cor_param` is numeric of length 1 and `times` is np array.
        ## Public attributes
        self.n = len(times)
        self.mean = mean
        self.cor_param = cor_param
        ## Private attributes (encapsulation)
        self._times = times
        self._current_U = False
        ## Some setup steps
        self._calc_mats()
        np.random.seed(seed)
    def __str__(self):    # 'print' method
        return f"An object of class `tsSimClass` with {self.n} time points."
    def __len__(self):
        return self.n

    ## Public methods: getter and setter (encapsulation)
    def set_times(self, new_times):
        self._times = new_times
        self._current_U = False
        self._calc_mats()
    def get_times(self):
        return self._times
 
    ## Main public method
    def simulate(self):
        if not self._current_U:    
            self._calc_mats()
        ## analogous to mu+sigma*z for generating N(mu, sigma^2)
        return self.mean + np.dot(self.U.T, np.random.normal(size = self.n))

    ## Private method.
    def _calc_mats(self):
        ## Calculates correlation matrix and Cholesky factor (caching).
        lag_mat = np.abs(self._times[:, np.newaxis] - self._times)
        cor_mat = np.exp(-lag_mat ** 2 / self.cor_param ** 2)
        self.U = np.linalg.cholesky(cor_mat)
        print("Done updating correlation matrix and Cholesky factor.")
        self._current_U = True
