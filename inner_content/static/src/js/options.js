/** @odoo-module **/
import options from "@web_editor/js/editor/snippets.options";

options.registry.s_inner_image_slider_options = options.Class.extend({
    // Method to add a slide
    addSlide: function (previewMode, widgetValue, params) {
        const $inner = this.$target.find('.carousel-inner');
        const $indicators = this.$target.find('.carousel-indicators');
        const slideCount = $inner.children('.carousel-item').length;

        $indicators.append(`<button type="button" data-bs-slide-to="${slideCount}"></button>`);

        $inner.append(`
            <div class="carousel-item">
                <img src="/web/image/website.s_carousel_default_image_1" class="d-block w-100" alt="New Slide"/>
            </div>
        `);
    },

    // Method to remove the last slide
    removeSlide: function (previewMode, widgetValue, params) {
        const $inner = this.$target.find('.carousel-inner');
        const $indicators = this.$target.find('.carousel-indicators');

        if ($inner.children('.carousel-item').length > 1) {
            $inner.children('.carousel-item').last().remove();$indicators.children('button').last().remove();

            // Re-assign 'active' class if the deleted slide was currently active
            if ($inner.find('.carousel-item.active').length === 0) {
                $inner.children('.carousel-item').first().addClass('active');$indicators.children('button').first().addClass('active');
            }
        }
    }
});
