/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.InnerImageSlider = publicWidget.Widget.extend({
    selector: '.s_inner_image_slider',
    start: function () {
        // Scope DOM operations to this specific snippet instance
        const $carousel = this.$('.custom-inner-carousel');

        // Generate a unique ID for this instance
        const uniqueId = 'carousel-' + new Date().getTime() + '-' + Math.floor(Math.random() * 1000);

        // Apply the ID and update navigation targets
        $carousel.attr('id', uniqueId);
        this.$('.carousel-control-prev, .carousel-control-next').attr('data-bs-target', '#' + uniqueId);
        this.$('.carousel-indicators button').attr('data-bs-target', '#' + uniqueId);

        return this._super.apply(this, arguments);
    }
});
