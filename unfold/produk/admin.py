from django.contrib import admin
from unfold.admin import ModelAdmin

from django.core.validators import EMPTY_VALUES
from django.utils.translation import gettext_lazy as _
from unfold.contrib.filters.admin import (
        TextFilter,
        FieldTextFilter,
        RangeDateFilter,
        RangeDateTimeFilter,
        AllValuesCheckboxFilter
    )
from unfold.paginator import InfinitePaginator
# Register your models here.
from . models import Barang, Pesanan, Pembelian

class CustomTextFilter(TextFilter):
    title = _("Custom filter Stock")
    parameter_name = "query_param_in_uri"

    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(stock=self.value())

        return queryset


@admin.register(Barang)
class BarangAdmin(ModelAdmin):
    list_display = ('nama', 'harga', 'stock')
    list_filter_submit = True 
    list_filter = [
        ("nama", FieldTextFilter),
        CustomTextFilter,
        ("harga", AllValuesCheckboxFilter)
    ]
    paginator = InfinitePaginator
    show_full_result_count = False


@admin.register(Pesanan)
class PesananAdmin(ModelAdmin):
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("tgl_pesanan", RangeDateFilter),  # Date filter
        ("tgl_pesanan", RangeDateTimeFilter),  # Datetime filter
    )
    list_display = ('pesanan_id', 'user', 'tgl_pesanan', 'status')

@admin.register(Pembelian)
class PembelianAdmin(ModelAdmin):
    list_display = ('pesans', 'barangs', 'quantity', 'total_harga')