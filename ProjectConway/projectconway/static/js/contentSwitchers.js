/**
 * JavaScript library the handles each button that switches between
 * different content in the pattern creation process.
 */

this.toScheduler = function() {
    /**
     * Switches the content row to the scheduler logic and aesthetics.
     */
    $("#success_popup").modal("hide");
    $("#content").load('/scheduler');
}