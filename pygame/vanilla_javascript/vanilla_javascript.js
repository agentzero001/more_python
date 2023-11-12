my_func = function(s) {
    return function(n) {
        var r = ''
        while (n > 0) {
            r += s;
            n--;
        }
        return r;
    }
}