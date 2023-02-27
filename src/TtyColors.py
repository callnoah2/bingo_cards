class TtyColors:  	  	  
    def black(self, s):  	  	  
        return "\x1b[1;30m{}\x1b[0m".format(s)  	  	  

    def red(self, s):  	  	  
        return "\x1b[1;31m{}\x1b[0m".format(s)  	  	  

    def green(self, s):  	  	  
        return "\x1b[1;32m{}\x1b[0m".format(s)  	  	  

    def yellow(self, s):  	  	  
        return "\x1b[1;33m{}\x1b[0m".format(s)  	  	  

    def blue(self, s):  	  	  
        return "\x1b[1;34m{}\x1b[0m".format(s)  	  	  

    def magenta(self, s):  	  	  
        return "\x1b[1;35m{}\x1b[0m".format(s)  	  	  

    def cyan(self, s):  	  	  
        return "\x1b[1;36m{}\x1b[0m".format(s)  	  	  

    def white(self, s):  	  	  
        return "\x1b[1;37m{}\x1b[0m".format(s)  	  	  
