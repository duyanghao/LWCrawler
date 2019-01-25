import time, os, stat

class CLogHelper():
    def __init__(self, log_file, file_cnt):
        self.fout         = 0
        self.log_file     = log_file        
        self.file_size    = 5 * 1024 * 1024        
        self.max_file_cnt = file_cnt		
		
    def __del__(self):
        self.close_log()
	
    def write_log(self, msg):     
        if self.fout == 0:
            return 0
        
        now_t = time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time()))

        strs = "[" + now_t + "]: " + msg + "\n"   
        #strs = msg + "\n"    
        self.fout.write(strs) 

        self.move_log_to_start()
        self.flush_log()
        
    def init_log(self):
		
        i = 0
        while i < 3:
            i += 1
			
            try:
                self.fout = open(self.log_file, 'a')
                break				
            except:
                self.fout = 0

        if i == 3:				
            print "init log: %s failed" % self.log_file             
            return -1
			
        return 0        
            
    def move_log_to_start(self):
		
        file_stats = os.stat(self.log_file)
        if file_stats[stat.ST_SIZE] > self.file_size:
		
            i = self.max_file_cnt 
            bak_file = "%s.%d" % (self.log_file, i)
            if os.path.isfile(bak_file) == True:
                os.remove(bak_file)

            i -= 1	
            while i > 0:
			
                src_file = "%s.%d" % (self.log_file, i)
                if os.path.isfile(src_file) == True:
                    dst_file = "%s.%d" % (self.log_file, i + 1) 			
                    os.rename(src_file, dst_file)

                i -= 1         	
	
            self.close_log()
            bak_file = "%s.%d" % (self.log_file, 1)	
            os.rename(self.log_file, bak_file)	
            
            ret = self.init_log() 	
            assert(ret == 0)
        
    def flush_log(self):
        if self.fout != 0:
            self.fout.flush()    

    def close_log(self):
        if self.fout != 0:
            self.fout.close()        
            print "close log_file %s" % self.log_file       
 	
if __name__=="__main__":
    obj = CLogHelper("../log/t", 10)
    obj.init_log()	
    obj.move_log_to_start()

