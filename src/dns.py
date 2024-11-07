
import dnslib
from dnslib.server import DNSHandler, DNSServer, DNSRecord, DNSLogger, BaseResolver
from collections import defaultdict

class AdBlockResolver(BaseResolver):
    def __init__(self, blocklist_file):
        self.blocklist = self.load_blocklist(blocklist_file)

    def load_blocklist(self, blocklist_file):
        blocklist = set()
        with open(blocklist_file, "r") as file:
            for line in file:
                domain = line.strip()
                blocklist.add(domain)
        return blocklist
    
    def resolve(self, request, handler):
        domain = str(request.q.qname)
        if domain in self.blocklist:
            reply = request.reply()
            reply.add_answer(dnslib.RR(request.q.qname, dnslib.QTYPE.A, rdata=dnslib.A("0.0.0.0")))
            return reply
        else:
            return super().resolve(request, handler)
        
class AdBlockDNSServer(DNSServer):
    def __init__(self, resolver, port=53, address=""):
        self.logger = DNSLogger(prefix=False)
        super().__init__(resolver, port=port, address=address, logger=self.logger)

if __name__ == "__main__":
    blocklist_file = "block.txt"  
    resolver = AdBlockResolver(blocklist_file)
    dns_server = AdBlockDNSServer(resolver)
    try:
        dns_server.start()
        print("DNS server is running. Ready to handle DNS requests.")
    except KeyboardInterrupt:
        pass
    finally:
        dns_server.stop()
    