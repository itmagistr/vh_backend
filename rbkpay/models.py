from django.db import models
from .utils import create_rbk_invoice
from django.utils import timezone
import json 

# Create your models here.
def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

class RBKEvent(models.Model):
	iid = models.CharField(max_length=20)
	dt = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20)
	metatxt = models.TextField()


class RBKInvoice(models.Model):
	iid = models.CharField(max_length=20)
	dt = models.DateTimeField(auto_now_add=True)
	expire = models.DateTimeField(default=one_day_hence)
	token = models.TextField(null=True, blank=True)
	status = models.CharField(max_length=20)
	event = models.ForeignKey(RBKEvent, null=False, blank=False, on_delete=models.CASCADE)
	amount = models.PositiveIntegerField(null=True, blank=True)
	title = models.CharField(max_length=35, null=True, blank=True)
	descr = models.CharField(max_length=255, null=True, blank=True)
	extra = models.TextField(null=True, blank=True)

	@classmethod
	def create(cls, title, price, desc, wishes):
		rbkinv = None
		inv = create_rbk_invoice(amount=100*price, product=title, desc=desc, wishes=wishes)
		if inv['code'] == 201:
			rbkEvent = RBKEvent(iid=inv['invoice']['iid'], status=inv['invoice']['istatus'], metatxt=json.dumps(inv['invoice'], indent=4))
			rbkEvent.save()
			rbkinv = cls(iid=inv['invoice']['iid'], title=title, descr=desc, amount=100*price, extra=wishes, 
						status=inv['invoice']['istatus'], expire=inv["invoice"]["dueDate"], token=inv['invoice']['token'], event=rbkEvent)
		return rbkinv


