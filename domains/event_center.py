from prots import *


@dataclass
class aCall:
    excutor:str
    operation:str
    args:tuple = field(default_factory=tuple)
    kwagrs:dict = field(default_factory=dict)
@dataclass
class aSubscribe:
    subscriber:str
    channel:str
@dataclass
class aChannel:
    name:str
    def __repr__(self):
        return str(self.name)
@dataclass
class aEvent:
    sub:str
    channel:str
    kwargs:dict

#=======================================================
class Caller():
    def __init__(self,callcenter) -> None:
        self.calls = Queue(1)
        self.callcenter:CallCenter = callcenter
    def call_excution(self,target_name,target_method,*args,**kws):
        my_call = (target_name,target_method,args,kws)
        self.calls.put(my_call)
        ret = self.callcenter.turn(self)
        return ret
    
class CallCenter():
    def __init__(self):
        self.excutors = dict([])
    def append_excutors(self,excutors:dict):
        self.excutors.update(excutors)
    def turn(self,caller):
        target_name,target_method,args,kws = caller.calls.get()
        excutor_operation = getattr(eval(target_name),target_method)
        return excutor_operation(*args,**kws)

# =======================================================
def entity_instance_locate(entity_name,modules):
    return modules.get(entity_name,None)

def get_cls_instance(cls,modules):
    _list = []
    for name,obj in modules.items():
        if isinstance(obj,cls):
            _list.append(name)
    return _list    


class Publisher():
    def __init__(self) -> None:
        self.events = Queue()
    def pub_event(self,sub,**kwargs):
        event = aEvent(sub=sub,kwargs=kwargs,channel=self.__class__.__name__)
        self.events.put(event)

class PartPublish():
    def __init__(self,_modules) -> None:
        self.channel_list = set(get_cls_instance(Publisher,_modules))
        self.channel_events = {}

   
    def pub_event_in_channel(self,channel:aChannel,event:aEvent):
        if channel not in self.channel_list:
            self.channel_list.append(channel)

class PartDispatch():

    def channel_message(self,channel,message):
        self.channels[channel] = message

    def broadcast(self):
        for subscriber in self.__subscribers:
            subscriber.watch(self)

class PartSubscribe():
    def __init__(self):
        self.channel_list = set()
        self.subscriber_subscribes = {}
        self.channel_subscribes = {}
    
    def attach_subscribe(self,subscribe:aSubscribe):
        try:
            self._attach_subscribe(subscribe)
        except Exception as e:
            logger.error(e)

    def _attach_subscribe(self,subscribe:aSubscribe):
        subscriber,channel = subscribe.subscribe,subscribe.channel
        if channel not in self.channel_list:
            raise ChannelNotExist
        _channels = self.subscriber_subscribes.get(subscribe.subscriber,set())
        _channels.add(channel)
        self.subscriber_subscribes.update({subscriber:_channels})
        
        _subscribers = self.channel_subscribers.get(channel,set())
        _subscribers.add(subscriber)
        self.channel_subscribers.update({channel:_subscribers})

    def attach_subscriber_subscribes(self,subscriber_subscribes:dict):
        for subscriber,channels in subscriber_subscribes.items():
            for channel in channels:
                subscribe = aSubscribe(subscriber,channel)
                self.attach_subscribe(subscribe)

    def attach_channel_subscribes(self,channel_subscribes:dict):
        for channel,subscribers in channel_subscribes.items():
            for subscriber in subscribers:
                subscribe = aSubscribe(subscriber,channel)
                self.attach_subscribe(subscribe)

    def detach_subscribe(self,subscribe:aSubscribe):
        _channels = self.subscriber_subscribes.pop(subscribe.subscriber,set())
        _channels.discard(subscribe.channel)
        self.subscriber_subscribes.update({subscribe.subscriber:_channels})

        _subscribers = self.channel_subscribes.pop(subscribe.channel,set())
        _subscribers.discard(subscribe.subscriber)
        self.channel_subscribes.update({subscribe.channel:_subscribers})

    

class MediaCenter(PartPublish,PartDispatch,PartSubscribe):
    def __init__(self,_modules):
        PartSubscribe.__init__(self)
        PartDispatch.__init__(self)
        PartPublish.__init__(self,_modules)
        pass

class ChannelNotExist(Exception):
    pass

# if __name__=="__main__":
#     upper_Alice = Publisher() #follower,foller/upper
#     publisher_Bob = Publisher() #subscriber,pubber/subber

#     class TestSelf():
#         def test_publish():
#             media_center = MediaCenter(globals())
#             print(media_center.channel_list)

#     TestSelf.test_publish()