<?php
/**
 * Add to the existing CFC REST snippet (or paste as a new Code Snippet).
 * Exposes GET/POST for Rank Math title + description on any page.
 */
add_action('rest_api_init', function () {
    register_rest_route('cfc/v1', '/seo/(?P<id>\d+)', [
        [
            'methods'  => 'GET',
            'callback' => function ($req) {
                $id = (int) $req['id'];
                return [
                    'id'          => $id,
                    'title'       => get_post_meta($id, 'rank_math_title', true),
                    'description' => get_post_meta($id, 'rank_math_description', true),
                    'focus_kw'    => get_post_meta($id, 'rank_math_focus_keyword', true),
                ];
            },
            'permission_callback' => function () { return current_user_can('edit_posts'); },
        ],
        [
            'methods'  => 'POST',
            'callback' => function ($req) {
                $id   = (int) $req['id'];
                $body = $req->get_json_params();
                if (isset($body['title']))       update_post_meta($id, 'rank_math_title', $body['title']);
                if (isset($body['description'])) update_post_meta($id, 'rank_math_description', $body['description']);
                if (isset($body['focus_kw']))    update_post_meta($id, 'rank_math_focus_keyword', $body['focus_kw']);
                return ['ok' => true, 'id' => $id];
            },
            'permission_callback' => function () { return current_user_can('edit_posts'); },
        ],
    ]);
});
