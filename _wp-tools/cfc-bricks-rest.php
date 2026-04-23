<?php
/**
 * Plugin Name: CFC Bricks REST
 * Description: Exposes raw Bricks page content meta via REST for programmatic content edits.
 * Version:     1.0.1
 * Author:      CFC
 *
 * Install: drop this file into /wp-content/mu-plugins/ (create folder if missing).
 * Then test:
 *   GET  /wp-json/cfc/v1/bricks/524  (with Basic auth of a user who can edit_posts)
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'rest_api_init', function () {

    register_rest_route( 'cfc/v1', '/bricks/(?P<id>\d+)', [
        'methods'             => 'GET',
        'permission_callback' => function () { return current_user_can( 'edit_posts' ); },
        'callback'            => function ( $req ) {
            $id = absint( $req['id'] );
            return [
                'content' => get_post_meta( $id, '_bricks_page_content_2', true ),
                'header'  => get_post_meta( $id, '_bricks_page_header_2',  true ),
                'footer'  => get_post_meta( $id, '_bricks_page_footer_2',  true ),
            ];
        },
    ] );

    register_rest_route( 'cfc/v1', '/bricks/(?P<id>\d+)', [
        'methods'             => 'POST',
        'permission_callback' => function () { return current_user_can( 'edit_posts' ); },
        'callback'            => function ( $req ) {
            $id = absint( $req['id'] );
            $p  = $req->get_json_params();
            if ( array_key_exists( 'content', $p ) ) {
                update_post_meta( $id, '_bricks_page_content_2', $p['content'] );
            }
            if ( array_key_exists( 'header', $p ) ) {
                update_post_meta( $id, '_bricks_page_header_2', $p['header'] );
            }
            if ( array_key_exists( 'footer', $p ) ) {
                update_post_meta( $id, '_bricks_page_footer_2', $p['footer'] );
            }
            // Clear caches where possible
            if ( function_exists( 'wp_cache_flush' ) ) { wp_cache_flush(); }
            if ( function_exists( 'rocket_clean_post' ) ) { rocket_clean_post( $id ); }
            return [ 'ok' => true, 'id' => $id ];
        },
    ] );

    register_rest_route( 'cfc/v1', '/seo/(?P<id>\d+)', [
        [
            'methods'             => 'GET',
            'permission_callback' => function () { return current_user_can( 'edit_posts' ); },
            'callback'            => function ( $req ) {
                $id = (int) $req['id'];
                return [
                    'title'       => get_post_meta( $id, 'rank_math_title',       true ),
                    'description' => get_post_meta( $id, 'rank_math_description', true ),
                    'focus'       => get_post_meta( $id, 'rank_math_focus_keyword', true ),
                ];
            },
        ],
        [
            'methods'             => 'POST',
            'permission_callback' => function () { return current_user_can( 'edit_posts' ); },
            'callback'            => function ( $req ) {
                $id = (int) $req['id'];
                $p  = $req->get_json_params();
                if ( array_key_exists( 'title',       $p ) ) update_post_meta( $id, 'rank_math_title',         $p['title'] );
                if ( array_key_exists( 'description', $p ) ) update_post_meta( $id, 'rank_math_description',   $p['description'] );
                if ( array_key_exists( 'focus',       $p ) ) update_post_meta( $id, 'rank_math_focus_keyword', $p['focus'] );
                return [ 'ok' => true, 'id' => $id ];
            },
        ],
    ] );

} );
