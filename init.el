(require 'package)

(let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))

                    (not (gnutls-available-p))))

       (url (concat (if no-ssl "http" "https") "://melpa.org/packages/")))

  (add-to-list 'package-archives (cons "melpa" url) t))

(when (< emacs-major-version 24)

  ;; For important compatibility libraries like cl-lib

  (add-to-list 'package-archives '("gnu" . "http://elpa.gnu.org/packages/")))

(add-to-list 'package-archives
             '("elpy" . "https://jorgenschaefer.github.io/packages/"))
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)

(package-initialize)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["#2d3743" "#ff4242" "#74af68" "#dbdb95" "#34cae2" "#008b8b" "#00ede1" "#e1e1e0"])
 '(custom-enabled-themes nil)
 '(package-selected-packages
   (quote
    (## flycheck-rust flycheck package-build shut-up epl git commander f dash s cask racer cargo rust-mode python-mode all-the-icons yasnippet-snippets auto-complete-c-headers auto-complete autopair))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(autopair-global-mode) ;; enable autopair in all buffers

(setq show-paren-delay 0)

(show-paren-mode 1)



(setq column-number-mode t)


(ac-config-default)


(defun my:ac-c-headers-init ()

  (require 'auto-complete-c-headers)

  (add-to-list 'ac-sources 'ac-source-c-headers))

(add-hook 'c++-mode-hook 'my:ac-c-headers-init)

(add-hook 'c-mode-hook 'my:ac-c-headers-init)


(setq-default c-basic-offset 4)


(yas-global-mode t)


(global-set-key [f8] 'neotree-toggle)
(setq neo-theme (if (display-graphic-p) 'icons 'arrow))


(elpy-enable)

(setq rust-format-on-save t)

(add-hook 'rust-mode-hook 'cargo-minor-mode)

(add-hook 'rust-mode-hook #'racer-mode)
(add-hook 'racer-mode-hook #'eldoc-mode)

(add-hook 'racer-mode-hook #'company-mode)

(require 'rust-mode)
(define-key rust-mode-map (kbd "TAB") #'company-indent-or-complete-common)
(setq company-tooltip-align-annotations t)

;; (use-package flycheck
;;   :ensure t
;;   :init (global-flycheck-mode))

(add-hook 'flycheck-mode-hook #'flycheck-rust-setup)
